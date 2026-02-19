<script setup>
import { useRouter } from 'vue-router'
import { useAuth } from '@/composables/useAuth'

const router = useRouter()
const { isAuthenticated, clearToken } = useAuth()

function logout() {
  clearToken()
  router.push('/login')
}
</script>

<template>
  <nav class="navbar">
    <RouterLink to="/home" class="brand">Crazy Charly Day</RouterLink>
    <div class="links">
      <RouterLink to="/home">Accueil</RouterLink>
      <RouterLink to="/articles">Catalogue</RouterLink>
      <template v-if="!isAuthenticated">
        <RouterLink to="/register">S'inscrire</RouterLink>
        <RouterLink to="/login">Connexion</RouterLink>
      </template>
      <template v-else>
        <button class="logout-btn" @click="logout">Déconnexion</button>
      </template>
    </div>
  </nav>

  <RouterView />
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 30px;
  border-bottom: 1px solid #ccc;
}

.brand {
  font-weight: bold;
  font-size: 18px;
  text-decoration: none;
  color: #333;
}

.links {
  display: flex;
  gap: 20px;
  align-items: center;
}

.links a {
  text-decoration: none;
  color: #333;
  font-size: 15px;
}

.links a.router-link-active {
  font-weight: bold;
  text-decoration: underline;
}

.logout-btn {
  background: none;
  border: 1px solid #c00;
  color: #c00;
  padding: 4px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 15px;
}

.logout-btn:hover {
  background: #c00;
  color: #fff;
}
</style>
