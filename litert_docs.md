# LiteRT Overview Documentation

Scraped from [https://ai.google.dev/edge/litert/overview](https://ai.google.dev/edge/litert/overview)

## Overview

- Home

- Google AI Edge

- LiteRT

LiteRT is Google's on-device framework for high-performance ML & GenAI
deployment on edge platforms, using efficient conversion, runtime, and
optimization.

The latest LiteRT 2.x release introduces the CompiledModel API,
a modern runtime interface designed to maximize hardware acceleration. While the Interpreter API (formerly TensorFlow Lite) remains available for backward
compatibility, the CompiledModel API is the recommended choice for developers
seeking state-of-the-art performance in on-device AI applications.

## Streamline development with LiteRT

Automated accelerator selection versus explicit delegate creation. Efficient I/O
buffer handling and async execution for superior performance.
See on-device inference documentation .

## Best-in-class GPU performance

Powered by ML Drift, now supporting both ML and Generative
AI models on GPUs APIs. See GPU acceleration documentation .

## Unified NPU acceleration

Accelerate your model using simplified NPU access from major
chipset providers. See NPU acceleration documentation .

## Superior LLM Support

LiteRT delivers high-performance deployment for Generative AI models across
mobile, desktop, and web platforms. See GenAI deployment documentation .

## Broad ML framework support

LiteRT supports streamlined conversion from PyTorch, TensorFlow, and JAX
Frameworks to .tflite or .litertlm format. See model conversion documentation .

## Get Started withCompiledModelAPI

- For classical ML models , see the following demo apps. Image segmentation Kotlin App : CPU/GPU/NPU inference. Image segmentation C++ App : CPU/GPU/NPU inference with async execution.

- For GenAI models , see the following demo apps: EmbeddingGemma semantic similarity C++ App :
CPU/GPU/NPU inference.

For classical ML models , see the following demo apps.

- Image segmentation Kotlin App : CPU/GPU/NPU inference.

- Image segmentation C++ App : CPU/GPU/NPU inference with async execution.

For GenAI models , see the following demo apps:

- EmbeddingGemma semantic similarity C++ App :
CPU/GPU/NPU inference.

## Development workflow

LiteRT runs inferences completely on-device on Android, iOS, Web, IoT, and on
desktop/laptop. Regardless of device, the following is the most common
workflow, with links to further instructions.

## Identify the most suitable solution to the ML challenge

LiteRT offers users a high level of flexibility and customizability when it
comes to solving machine learning problems, making it a good fit for users who
require a specific model or a specialized implementation. Users looking for
plug-and-play solutions may prefer MediaPipe
Tasks ,
which provides ready-made
solutions for common machine learning tasks like object detection,
text classification, and LLM inference.

## Obtain and preparing the model

A LiteRT model is represented in an efficient portable format known as FlatBuffers , which uses the .tflite file extension.

You can obtain a LiteRT model in the following ways:

- Obtain a pre-trained model: for popular ML workloads like Image
segmentation, Object detection etc. The simplest approach is to use a LiteRT model already in the .tflite format. These models don't require any added conversion steps. Model type Pre-trained model source Classical ML ( .tflite format) Visit Kaggle or HuggingFace E.g. Image segmentation models and sample app Generative AI ( .litertlm format) LiteRT Hugging Face page E.g. Gemma Family

- Convert your chosen PyTorch,
TensorFlow or JAX model into a LiteRT model if you choose to not use a
pre-trained model. [PRO USER] Model framework Sample models Conversion tool Pytorch Hugging Face Torchvision Link TensorFlow Kaggle Models Hugging Face Link Jax Hugging Face Link

- Author your LLM for further optimization using Generative
API [PRO USER] Our Generative API library provides PyTorch built-in building blocks for
composing Transformer models such as Gemma , TinyLlama and others using mobile-friendly abstractions, through which
we can guarantee conversion,
and performant execution on our mobile runtime, LiteRT. See Generative API
documentation .

Obtain a pre-trained model: for popular ML workloads like Image
segmentation, Object detection etc.

The simplest approach is to use a LiteRT model already in the .tflite format. These models don't require any added conversion steps.

Convert your chosen PyTorch,
TensorFlow or JAX model into a LiteRT model if you choose to not use a
pre-trained model. [PRO USER]

Author your LLM for further optimization using Generative
API [PRO USER]

Our Generative API library provides PyTorch built-in building blocks for
composing Transformer models such as Gemma , TinyLlama and others using mobile-friendly abstractions, through which
we can guarantee conversion,
and performant execution on our mobile runtime, LiteRT. See Generative API
documentation .

## Optimize [PRO USER]

AI Edge Quantizer for advanced developers is a tool to quantize converted
LiteRT models. It aims to facilitate advanced users to strive for optimal
performance on resource demanding models (e.g., GenAI models).

See more details from AI Edge Quantizer documentation .

## Integrate the model into your app on edge platforms

LiteRT lets you to run ML models entirely on-device with high performance
across Android, iOS, Web, Desktop, and IoT platforms.

Use the following guides to integrate a LiteRT model on your preferred platform:

The following code snippets show a basic implementation in
Kotlin and C++.

## Kotlin

```
// Load model and initialize runtimevalcompiledModel=CompiledModel.create("/path/to/mymodel.tflite",CompiledModel.Options(Accelerator.CPU))// Preallocate input/output buffersvalinputBuffers=compiledModel.createInputBuffers()valoutputBuffers=compiledModel.createOutputBuffers()// Fill the input bufferinputBuffers.get(0).writeFloat(input0)inputBuffers.get(1).writeFloat(input1)// InvokecompiledModel.run(inputBuffers,outputBuffers)// Read the outputvaloutput=outputBuffers.get(0).readFloat()
```

## C++

```
// Load model and initialize runtimeLITERT_ASSIGN_OR_RETURN(autoenv,GetEnvironment());LITERT_ASSIGN_OR_RETURN(autooptions,GetOptions());LITERT_ASSIGN_OR_RETURN(autocompiled_model,CompiledModel::Create(env,"/path/to/mymodel.tflite",options));// Preallocate input/output buffersLITERT_ASSIGN_OR_RETURN(autoinput_buffers,compiled_model.CreateInputBuffers(signature_index));LITERT_ASSIGN_OR_RETURN(autooutput_buffers,compiled_model.CreateOutputBuffers(signature_index));// Fill the input bufferLITERT_ABORT_IF_ERROR(input_buffers[0].Write(input0));LITERT_ABORT_IF_ERROR(input_buffers[1].Write(input1));// InvokeLITERT_ABORT_IF_ERROR(compiled_model.Run(signature_index,input_buffers,output_buffers));// Read the outputLITERT_ABORT_IF_ERROR(output_buffers[0].Read(output0));
```

## Choose a backend

The most straightforward way to incorporate backends in LiteRT is to rely on
the runtime's built-in intelligence. With the CompiledModel API, LiteRT
simplifies the setup significantly with the ability to specify the
target backend as an option. See on-device inference guide for more
details.

## Additional documentation and support

- LiteRT-Samples GitHub Repo for more LiteRT sample apps.

- For existing users of TensorFlow Lite , see migration guide .

- LiteRT Tools page for performance, profiling, error reporting etc.

LiteRT-Samples GitHub Repo for more LiteRT sample apps.

For existing users of TensorFlow Lite , see migration guide .

LiteRT Tools page for performance, profiling, error reporting etc.
