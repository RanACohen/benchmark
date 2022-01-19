from torchbenchmark.util.framework.vision.model_factory import TorchVisionModel
from torchbenchmark.tasks import COMPUTER_VISION

class Model(TorchVisionModel):
    task = COMPUTER_VISION.CLASSIFICATION

    def __init__(self, device=None, jit=False, fuser="", train_bs=64, eval_bs=64, extra_args=[]):
        super().__init__(model_name="shufflenet_v2_x1_0", device=device, jit=jit, fuser=fuser,
                         train_bs=train_bs, eval_bs=eval_bs, extra_args=extra_args)
