class Job:
    def __init__(self, name: str, full_name: str, url: str, build_count: int):
        self.build_count = build_count
        self.full_name = full_name
        self.name = name
        self.url = url

    def __repr__(self):
        return self.full_name


def parse_job(data):
    return Job(
        name=data['name'],
        full_name=data['fullName'],
        build_count=len(data['builds']),
        url=data['url']
    )
