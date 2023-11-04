<template>
<header>
  <nav class="bg-gray-800 p-4">
    <div class="container mx-auto flex justify-between items-center">
      <!-- Logo or Brand -->
      <div class="text-white text-lg font-semibold">
        My Logo
      </div>

      <!-- Navigation Links -->
      <div class="space-x-4">
        <router-link to="/" class="text-white">หน้าคำนวน</router-link>
        <router-link to="/about" class="text-white">about</router-link> 
        <router-link to="/contact" class="text-white">Contact</router-link>
      </div>
    </div>
  </nav>
  </header> 
</template>

<script>
export default {
  name: 'Navbar-t', 
};
</script>

<style scoped>
/* You can add additional styles specific to this component if needed */
</style>
 