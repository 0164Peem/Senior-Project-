<!--<template>
  <InputForm/>
</template>

<script>
import InputForm from './views/InputForm.vue' 

export default {
  name: 'App',
  components: {
    InputForm
  }
}
</script>-->
<template>
<header>
<NavBar></NavBar>
</header>
   <main>
    <router-view></router-view>
  </main>

    
  
</template>

<script setup>
import NavBar from './components/NavBar.vue' 


</script>


<style>
#app {
  
 
}
body{
  margin: 0 ;
  background: #eee ;   

}
</style>
