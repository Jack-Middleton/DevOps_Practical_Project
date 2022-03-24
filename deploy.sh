docker stack deploy --compose-file docker-compose.yaml fun-proj-stack
docker service update --replicas 3 fun-proj-stack_flask-app