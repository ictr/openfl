#!/bin/bash
set -e

fx envoy start -n envoy2 --disable-tls --envoy-config-path envoy_config.yaml -dh localhost -dp 50050
