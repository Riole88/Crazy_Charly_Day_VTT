<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import jouetImg from '../../assets/images.jfif'
import { categoriesLabel, tranchesLabel, etatsLabel } from '@/constants/articles'

const API = import.meta.env.VITE_API
const router = useRouter()

const articles = ref([])
const loading = ref(true)
const error = ref('')
const page = ref(1)
const perPage = 10

const totalPages = computed(() => Math.ceil(articles.value.length / perPage))

const paginated = computed(() => {
  const start = (page.value - 1) * perPage
  return articles.value.slice(start, start + perPage)
})

onMounted(async () => {
  try {
    const res = await fetch(`${API}/articles`)
    if (!res.ok) throw new Error('Erreur serveur')
    articles.value = await res.json()
  } catch (e) {
    error.value = 'Impossible de charger les articles.'
    console.error(e)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="container">
    <h2>Catalogue des articles</h2>

    <p v-if="loading" class="info">Chargement...</p>
    <p v-else-if="error" class="error">{{ error }}</p>

    <template v-else>
      <div class="header-actions">
        <p class="count">{{ articles.length }} article(s) disponible(s)</p>
        <button class="btn-add" @click="router.push('/articles/create')">+ Ajouter un article</button>
      </div>

      <div class="grid">
        <div v-for="article in paginated" :key="article.id" class="card" @click="router.push(`/articles/${article.id}`)" style="cursor:pointer">
          <img :src="jouetImg" :alt="article.designation" class="card-img" />
          <div class="card-body">
            <h3 class="card-title">{{ article.designation }}</h3>
            <div class="card-tags">
              <span class="badge cat">{{ article.category }} — {{ categoriesLabel[article.category] }}</span>
              <span class="badge age">{{ article.age }} · {{ tranchesLabel[article.age] }}</span>
              <span class="badge etat">{{ etatsLabel[article.state] ?? article.state }}</span>
            </div>
            <div class="card-footer">
              <span class="prix">{{ article.price }} €</span>
              <span class="poids">{{ article.weight }} g</span>
            </div>
          </div>
        </div>

        <p v-if="paginated.length === 0" class="empty">Aucun article disponible.</p>
      </div>

      <!-- Pagination -->
      <div class="pagination" v-if="totalPages > 1">
        <button @click="page--" :disabled="page === 1">‹ Précédent</button>
        <span>Page {{ page }} / {{ totalPages }}</span>
        <button @click="page++" :disabled="page === totalPages">Suivant ›</button>
      </div>
    </template>
  </div>
</template>

<style scoped>
.container {
  max-width: 1000px;
  margin: 40px auto;
  padding: 0 20px;
}

h2 {
  margin-bottom: 16px;
}

.count {
  font-size: 14px;
  color: #666;
}

.header-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.btn-add {
  padding: 8px 16px;
  background: #333;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.btn-add:hover {
  background: #555;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  background: #fff;
}

.card-img {
  width: 100%;
  height: 150px;
  object-fit: cover;
}

.card-body {
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}

.card-title {
  font-size: 15px;
  font-weight: bold;
  margin: 0;
}

.card-tags {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.badge {
  display: inline-block;
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 12px;
  background: #eee;
}

.badge.cat { background: #e8f0fe; color: #1a56db; }
.badge.age { background: #fef3c7; color: #92400e; }
.badge.etat { background: #d1fae5; color: #065f46; }

.card-footer {
  display: flex;
  justify-content: space-between;
  margin-top: auto;
  font-size: 14px;
  font-weight: bold;
  color: #333;
}

.poids {
  color: #888;
  font-weight: normal;
}

.empty {
  text-align: center;
  color: #999;
  padding: 20px;
  grid-column: 1 / -1;
}

/* Pagination */
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin-top: 30px;
}

.pagination button {
  padding: 8px 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background: white;
  cursor: pointer;
  font-size: 14px;
}

.pagination button:disabled {
  opacity: 0.4;
  cursor: default;
}

.info { color: #666; }
.error { color: #c62828; }

@media (max-width: 600px) {
  .grid {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
}
</style>
