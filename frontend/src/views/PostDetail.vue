<template>
    <div class="relative py-16  overflow-hidden">

    <div class="relative px-4 sm:px-6 lg:px-8">
      <div class="text-lg max-w-prose mx-auto">
        <h1>
          <span class="mt-2 block text-3xl text-center leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">{{ $route.params.title }}</span>
        </h1>
        <p class="mt-8 text-xl text-gray-500 leading-8">{{ $route.params.slug }}</p>
      </div>
      <div class="mt-6 prose prose-indigo prose-lg text-gray-500 mx-auto">
        {{ $route.params.content }}
      </div>
    </div>
  </div>
</template>