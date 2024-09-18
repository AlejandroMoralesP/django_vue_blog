<template>
  <div class="relative bg-gray-50 pt-16 pb-20 px-4 sm:px-6 lg:pt-24 lg:pb-28 lg:px-8">
    <div class="absolute inset-0">
      <div class="bg-white h-1/3 sm:h-2/3" />
    </div>
    <div class="relative max-w-7x1 mx-auto">
      <div class="text-center">
        <h2 class="text-3x1 tracking-tight font-extrabold text-gray-900 sm:text-4x1">
          Admin Post List
        </h2>
        <p class="mt-3 max-w-2x1 mx-auto text-x1 text-gray-500 sm:mt-4">
          Reverse ordering
        </p>
      </div>
      <div class="mt-12 max-w-lg mx-auto grid gap-5 lg:grid-cols-3 lg:max-w-none">
        <div v-for="post in posts" :key="post.id" class="flex flex-col rounded-lg shadow-lg overflow-hidden">
          <p>{{ post.title }}</p>
          <p>{{ post.content }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getAPI } from '../axios-api'

export default {
  name: 'Blog',
  data() {
    return {
      posts: []
    }
  },
  created () {
    getAPI.get('/blog/posts/',)
      .then(response => {
        console.log('Post API has recieved data')
        this.posts = response.data
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>