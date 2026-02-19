<script setup>
import { useAuth } from '@/composables/useAuth'

const { isAuthenticated } = useAuth()
</script>

<template>
  <div class="container">
    <h1>Bienvenue sur Crazy Charly Day</h1>
    <template v-if="!isAuthenticated">
      <p>Connecte-toi pour commencer à jouer.</p>
      <RouterLink to="/login">Se connecter</RouterLink>
    </template>
    <template v-else>
      <p>Bonne continuation sur la plateforme !</p>
      <RouterLink to="/articles">Voir le catalogue</RouterLink>
    </template>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 60px auto;
  padding: 30px;
  text-align: center;
}

a {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 24px;
  background: #333;
  color: white;
  border-radius: 4px;
  text-decoration: none;
}

a:hover {
  background: #555;
}
</style>