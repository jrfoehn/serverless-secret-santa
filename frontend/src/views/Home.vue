<template>
  <div>
    <secret-santa msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import SecretSanta from "@/components/SecretSanta.vue";

export default {
  name: "home",
  components: {
    SecretSanta
  }
};
</script>
