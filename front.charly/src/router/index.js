import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Articles from '@/views/Articles.vue'
import ArticleDetail from '@/views/ArticleDetail.vue'
import CreateArticle from '@/views/CreateArticle.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'root', redirect: '/home' },
    { path: '/home', name: 'home', component: Home },
    { path: '/register', name: 'register', component: Register },
    { path: '/login', name: 'login', component: Login },
    { path: '/articles', name: 'articles', component: Articles },
    { path: '/articles/create', name: 'article-create', component: CreateArticle },
    { path: '/articles/:id', name: 'article-detail', component: ArticleDetail },
  ],
})

export default router