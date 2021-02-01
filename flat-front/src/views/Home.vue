<template>
  <div class="home">
    <h1 class="header">Flat Test</h1>
    <ul class="collection with-header">
      <li class="collection-header"><h4>Branches</h4></li>
      <li v-for="branch in branches" :key="branch" class="collection-item">
        <label @click="toMerge(branch)" :id="branch"></label>
        <p @click="goToCommits(branch)">{{branch}}</p>
      </li>
    </ul>
    <button @click="mergeBranches()" type="button" :class="{'disabled': !mergeButton}" class="waves-effect waves-light btn">Merge Branches</button>
  </div>
</template>

<style scoped>
button {
  margin-bottom: 3rem;
}

label {
  position: absolute;
  left: 30px;
  margin-top: 1rem;
  border: 1px solid rgb(110, 110, 110);
  width: 2rem;
  height: 2rem;
}

li > p {
  cursor: pointer;
}

.collection {
  width: 30%;
  margin-left: 35%;
  border: 1px solid rgb(6, 146, 6)
}

.collection > .collection-item {
  margin: 1rem;
  margin-left: 2.5rem;
}

.collection > .collection-item > p:hover {
  border: thick double rgb(55, 91, 145);
  background-color: rgb(211, 225, 240);
}
</style>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      branches: null,
      commits: null,
      items_to_merge : [],
      mergeButton: false
    }
  },

  name: 'Home',

  components: {},

  methods: {
    getBranches() {
      axios.get('http://127.0.0.1:5000/branches/')
    .then(res => {
      this.branches = res.data
    })
    .catch(err => console.dir(err))
    },

    goToCommits(branch) {
      this.$router.push({path: `/branch/${branch}`})
    },

    toMerge(branch) {
      let label = document.getElementById(branch)
      if (!this.items_to_merge.find(el => el === branch)) {
        if (this.items_to_merge.length === 2) {
          let old_branch = this.items_to_merge.shift()
          document.getElementById(old_branch).style.backgroundColor = "#fff"
        }
        this.items_to_merge.push(branch)
        label.style.backgroundColor = "#26a69a"
      } else {
        let index = this.items_to_merge.indexOf(branch)
        this.items_to_merge.splice(index, 1)
        label.style.backgroundColor = "#fff"
      }
    },

    mergeBranches() {
      let data = {
        "branch1": this.items_to_merge[0],
        "branch2": this.items_to_merge[1]
      }
      axios.post(`http://127.0.0.1:5000/branches/merge/${JSON.stringify(data)}`)
      .then(res => console.log(res))
      .catch(err => console.log(err))
    }
  },

  watch: {
    items_to_merge() {
      if (this.items_to_merge.length === 2) {
        this.mergeButton = true
      } else {
        this.mergeButton = false
      }
    }
  },

  created() {
    this.getBranches()
  }
}
</script>
