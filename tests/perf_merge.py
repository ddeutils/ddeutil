from ddeutil.core import merge

try:
    import perfplot
except ImportError as err:
    raise ImportError(
        "Please install perfplot for this testing perf script with\n\t\t"
        "pip install -U perfplot"
    ) from err


class MergePerfTest:
    def __init__(self):
        self.merge_dict = self.perf_merge_dict()

    @staticmethod
    def perf_merge_dict():
        return perfplot.bench(
            setup=lambda n: [
                {f"{2 * n}": 2 * n for n in range(n)},
                {f"{2 * n+1}": 2 * n + 1 for n in range(n)},
            ],
            kernels=[
                lambda n: merge.merge_dict(n[0], n[1], mode="chain"),
                lambda n: merge.merge_dict(n[0], n[1], mode="update"),
                lambda n: merge.merge_dict(n[0], n[1], mode="reduce"),
            ],
            labels=["chain", "update", "reduce"],
            n_range=[2**k for k in range(15)],
            xlabel="len of dict",
            equality_check=lambda x, y: dict(x) == dict(y),
            show_progress=True,
            max_time=None,
        )

    def show(self):
        self.merge_dict.show()

    def save(self):
        self.merge_dict.save(
            "img/perf_merge_dict.png", transparent=True, bbox_inches="tight"
        )


if __name__ == "__main__":
    MergePerfTest().save()
