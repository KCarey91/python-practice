# check_container.py
from typing import Optional
from gmail_alert import SendGmailForServiceDown
import docker


def is_container_running(container_name: str) -> Optional[bool]:
    """Verify the status of a container by it's name

    :param container_name: the name of the container
    :return: boolean or None
    """
    RUNNING = "running"
    # Connect to Docker using the default socket or the configuration
    # in your environment
    docker_client = docker.from_env()
    # Or give configuration
    # docker_socket = "unix://var/run/docker.sock"
    # docker_client = docker.DockerClient(docker_socket)

    try:
        container = docker_client.containers.get(container_name)
    except docker.errors.NotFound as exc:
        print(f"Check container name!\n{exc.explanation}")
    else:
        container_state = container.attrs["State"]
        return container_state["Status"] == RUNNING


if __name__ == "__main__":
    container_name = "webserver"
    result = is_container_running(container_name)
    if result:
        print("Nginx is running")
    else:
        nginx = SendGmailForServiceDown.main("Nginx")
