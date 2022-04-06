from torchbenchmark.util.framework.vision.model_factory import TorchVisionModel
from torchbenchmark.tasks import COMPUTER_VISION

class Model(TorchVisionModel):
    task = COMPUTER_VISION.CLASSIFICATION

    def __init__(self, device=None, jit=False, fuser="", dtype="fp32", train_bs=1, eval_bs=1, extra_args=[]):
        super().__init__(model_name="resnet50", device=device, jit=jit, fuser=fuser, dtype=dtype,
                         train_bs=train_bs, eval_bs=eval_bs, extra_args=extra_args)
