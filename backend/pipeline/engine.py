class PipelineEngine:
    def __init__(self, stages):
        self.stages = stages

    def run(self, input_data):
        data = input_data

        for stage in self.stages:
            data = stage.run(data)

            if data is None:
                return {"error": f"{stage.__class__.__name__} failed"}

        return data