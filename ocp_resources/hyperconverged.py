from ocp_resources.resource import NamespacedResource


class HyperConverged(NamespacedResource):
    api_group = NamespacedResource.ApiGroup.HCO_KUBEVIRT_IO

    def __init__(
        self,
        name,
        namespace,
        client=None,
        infra=None,
        workloads=None,
        teardown=True,
    ):
        super().__init__(
            name=name, namespace=namespace, client=client, teardown=teardown
        )
        self.infra = infra
        self.workloads = workloads

    def to_dict(self):
        res = super().to_dict()

        if self.infra:
            res.setdefault("spec", {}).setdefault("infra", {}).update(self.infra)

        if self.workloads:
            res.setdefault("spec", {}).setdefault("workloads", {}).update(
                self.workloads
            )

        return res
