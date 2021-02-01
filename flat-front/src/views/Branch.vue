<template>
  <div class="about">
    <h1>This is the branch: {{name}}</h1>
    <!--These are going to be on the Branch detail view -->
    <div v-for="commit in commits" :key="commit.commit">
      <repo-card :commit="commit" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import RepoCard from '@/components/RepoCard.vue'
import axios from 'axios'

export default {
  data() {
    return {
      name: null,
      commits: null
    }
  },

  components: {
    RepoCard
  },

  methods: {
    getCommits(branch) {
      axios.get(`${axios.defaults.baseURL}commits/${branch}`)
      .then(res => {
        this.commits = res.data
      })
      .catch(err => console.log(err))
    }
  }, 
  
  created() {
    this.name = this.$route.params.name
    this.getCommits(this.name)
  }
}
</script>
