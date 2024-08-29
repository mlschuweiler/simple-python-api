#!/bin/zsh

destination_cluster=$1

kubectx $destination_cluster
kubectl delete -f ./manifests/$destination_cluster/service.yaml
kubectl apply -f ./manifests/$destination_cluster/service.yaml #--dry-run

## Currently not working. Aborting for speed. Revisit for "controlled" deployments
# input_statement="Apply Change? [Y/n]:"
# read -p "$input_statement" -s apply
# echo "Entered: $apply"

# if [[ $apply == 'Y' || $apply == 'y' ]]; then
#     echo "[+] Applying change..."
#     # kubectl apply -f ./manifests/$destination_cluster/service.yaml
#     echo "[+] Complete!"
# else
#     echo "[+] Denied.. Aborting..."
# fi
