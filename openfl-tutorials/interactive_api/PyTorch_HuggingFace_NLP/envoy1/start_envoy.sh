#!/bin/bash
set -e

fx envoy start -n envoy1 --disable-tls --envoy-config-path envoy_config.yaml -dh localhost -dp 50050
