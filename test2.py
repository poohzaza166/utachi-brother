# import torch
# from torch import autocast
# from diffusers import StableDiffusionPipeline
# from pprint import pprint

# pipe = StableDiffusionPipeline.from_pretrained(
#     'hakurei/waifu-diffusion',
#     torch_dtype=torch.float32
# ).to('cuda')
# pipe.safety_checker = lambda images, clip_input: (images, False)
# prompt = "futanari girl with a horse cock"
# with autocast("cuda"):
#     image = pipe(prompt, guidance_scale=17)['sample'][0]  
#     # images = pipe(prompt, guidance_scale=5)
#     # pprint(images)
#     # image = images
    
# image.save("testv1.png")

import torch
torch.cuda.empty_cache()
from torch import autocast
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    'hakurei/waifu-diffusion',
    torch_dtype=torch.float16, revision='fp16'
)

pipe.to("cuda")

prompt = "1girl, aqua eyes, baseball cap, blonde hair, closed mouth, earrings, green background, hat, hoop earrings, jewelry, looking at viewer, shirt, short hair, simple background, solo, upper body, yellow shirt"
with autocast("cuda"):
    image = pipe(prompt, guidance_scale=6)["sample"][0]  
    
image.save("test.png")
