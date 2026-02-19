<script setup></script>

<template>
  <nav class="navbar">
    <RouterLink to="/home" class="brand">Crazy Charly Day</RouterLink>
    <div class="links">
      <RouterLink to="/home">Accueil</RouterLink>
      <RouterLink to="/articles">Catalogue</RouterLink>
      <RouterLink to="/register">S'inscrire</RouterLink>
      <RouterLink to="/login">Connexion</RouterLink>
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
</style>
