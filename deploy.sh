#!/bin/bash

set -e

HETZNER_API_TOKEN=$1
TAILSCALE_AUTH_KEY=$2
GITHUB_TOKEN=$3
GITHUB_REPO=$4 

echo "🚀 Creating Hetzner VPS..."

REG_TOKEN=$(curl -s -X POST \
  -H "Authorization: token ${GITHUB_TOKEN}" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/${GITHUB_REPO}/actions/runners/registration-token" \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['token'])")

echo "✅ Got GitHub runner registration token"

CLOUD_INIT=$(cat <<EOF
#!/bin/bash
set -e

apt-get update -q
apt-get install -y -q curl python3 python3-pip git

curl -fsSL https://tailscale.com/install.sh | sh
tailscale up --authkey="${TAILSCALE_AUTH_KEY}" --hostname="hetzner-runner" --accept-routes

echo "✅ Tailscale connected"

useradd -m -s /bin/bash runner || true

cd /home/runner
mkdir -p actions-runner && cd actions-runner

curl -o actions-runner-linux-x64.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.317.0/actions-runner-linux-x64-2.317.0.tar.gz
tar xzf actions-runner-linux-x64.tar.gz
rm actions-runner-linux-x64.tar.gz

chown -R runner:runner /home/runner/actions-runner

sudo -u runner ./config.sh \
  --url "https://github.com/${GITHUB_REPO}" \
  --token "${REG_TOKEN}" \
  --name "hetzner-ephemeral" \
  --labels "hetzner-runner" \
  --unattended \
  --ephemeral

sudo -u runner ./run.sh
EOF
)

RESPONSE=$(curl -s -X POST \
  -H "Authorization: Bearer ${HETZNER_API_TOKEN}" \
  -H "Content-Type: application/json" \
  "https://api.hetzner.cloud/v1/servers" \
  -d "{
    \"name\": \"github-runner-$(date +%s)\",
    \"server_type\": \"cx23\",
    \"image\": \"ubuntu-24.04\",
    \"location\": \"nbg1\",
    \"user_data\": $(echo "$CLOUD_INIT" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read()))')
  }")

echo "Hetzner response: $RESPONSE"

SERVER_ID=$(echo $RESPONSE | python3 -c "import sys,json; print(json.load(sys.stdin)['server']['id'])")

echo "✅ VPS created with ID: ${SERVER_ID}"
echo "server_id=${SERVER_ID}" >> $GITHUB_OUTPUT
echo "✅ VPS ID ${SERVER_ID} saved to outputs"
