# -*- coding: utf-8 -*-

from ocp_resources.resource import Resource


class HostPathProvisioner(Resource):
    """
    HostPathProvisioner Custom Resource Object.
    """

    api_group = Resource.ApiGroup.HOSTPATHPROVISIONER_KUBEVIRT_IO

    class Name:
        HOSTPATH_PROVISIONER = "hostpath-provisioner"

    def __init__(
        self, name, path=None, image_pull_policy=None, client=None, teardown=True
    ):
        super().__init__(name=name, client=client, teardown=teardown)
        self.path = path
        self.image_pull_policy = image_pull_policy

    def to_dict(self):
        res = super().to_dict()
        spec = res.setdefault("spec", {})
        path_config = spec.setdefault("pathConfig", {})
        if self.path:
            path_config["path"] = self.path
        if self.image_pull_policy:
            spec["imagePullPolicy"] = self.image_pull_policy
        return res

    @property
    def volume_path(self):
        return self.instance.spec.pathConfig.path
