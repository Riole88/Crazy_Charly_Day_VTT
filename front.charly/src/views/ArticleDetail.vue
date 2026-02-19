<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import jouetImg from '../../assets/images.jfif'
import { categoriesLabel, tranchesLabel, etatsLabel } from '@/constants/articles'

const API = import.meta.env.VITE_API
const route = useRoute()
const router = useRouter()

const article = ref(null)
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const res = await fetch(`${API}/articles/${route.params.id}`)
    if (!res.ok) throw new Error('Article introuvable')
    article.value = await res.json()
  } catch (e) {
    error.value = "Impossible de charger l'article."
    console.error(e)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="container">
    <button class="btn-retour" @click="router.push('/articles')">← Retour au catalogue</button>

    <p v-if="loading" class="info">Chargement...</p>
    <p v-else-if="error" class="error">{{ error }}</p>

    <div v-else class="detail">
      <img :src="jouetImg" :alt="article.designation" class="detail-img" />

      <div class="detail-body">
        <h2>{{ article.designation }}</h2>

        <button class="btn-edit" @click="router.push(`/articles/${route.params.id}/edit`)">Modifier</button>

        <table class="info-table">
          <tbody>
            <tr>
              <th>Catégorie</th>
              <td>
                <span class="badge cat">{{ article.category }}</span>
                {{ categoriesLabel[article.category] }}
              </td>
            </tr>
            <tr>
              <th>Tranche d'âge</th>
              <td>
                <span class="badge age">{{ article.age }}</span>
                {{ tranchesLabel[article.age] }}
              </td>
            </tr>
            <tr>
              <th>État</th>
              <td>
                <span class="badge etat">{{ etatsLabel[article.state] ?? article.state }}</span>
              </td>
            </tr>
            <tr>
              <th>Prix</th>
              <td><strong>{{ article.price }} €</strong></td>
            </tr>
            <tr>
              <th>Poids</th>
              <td>{{ article.weight }} g</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: 40px auto;
  padding: 0 20px;
}

.btn-retour {
  background: none;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 8px 14px;
  cursor: pointer;
  font-size: 14px;
  margin-bottom: 24px;
  color: #333;
}

.btn-retour:hover {
  background: #f5f5f5;
}

.btn-edit {
  display: inline-block;
  margin-bottom: 16px;
  padding: 8px 14px;
  background: #333;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.btn-edit:hover {
  background: #555;
}

.detail {
  display: flex;
  gap: 32px;
  align-items: flex-start;
}

.detail-img {
  width: 260px;
  height: 260px;
  object-fit: cover;
  border-radius: 8px;
  border: 1px solid #ddd;
  flex-shrink: 0;
}

.detail-body {
  flex: 1;
}

.detail-body h2 {
  margin: 0 0 20px;
  font-size: 22px;
}

.info-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 15px;
}

.info-table th,
.info-table td {
  padding: 10px 12px;
  border-bottom: 1px solid #eee;
  text-align: left;
}

.info-table th {
  color: #666;
  font-weight: 600;
  width: 140px;
}

.badge {
  display: inline-block;
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 12px;
  margin-right: 6px;
}

.badge.cat  { background: #e8f0fe; color: #1a56db; }
.badge.age  { background: #fef3c7; color: #92400e; }
.badge.etat { background: #d1fae5; color: #065f46; }

.info { color: #666; }
.error { color: #c62828; }

@media (max-width: 600px) {
  .detail {
    flex-direction: column;
  }

  .detail-img {
    width: 100%;
    height: 220px;
  }
}
</style>
