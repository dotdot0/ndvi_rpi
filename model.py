import replicate

image = open("./color_mapped_image.png", 'rb')

input = {
    "image": image,
    "prompt": "Calculate the ndvi from the above image"
}

output = replicate.run(
    "yorickvp/llava-v1.6-34b:41ecfbfb261e6c1adf3ad896c9066ca98346996d7c4045c5bc944a79d430f174",
    input=input
)
print("".join(output))
#=> "The image shows a person ironing clothes on an ironing b...
