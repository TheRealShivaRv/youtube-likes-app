<template>
  <div class="container">
    <div class="app_head">
      <h1>{{title}}</h1>
      <ul class="link_list">
        <li @click="toggleComps('browse')">Browse</li>
        <li @click="toggleComps('likes')">Likes</li>
      </ul>
    </div>
    <BrowseVideos :searches="searchedVideos" @searchTerm="getVideosFromYoutube($event)" @videoLike="likeVideo($event)"/>
    <LikedVideos  :likedVideosList="likedVideos" @unlikeVideo="unlinkVideoFn($event)"/>
  </div>
</template>

<script>
import BrowseVideos from './components/BrowseVideos.vue'
import LikedVideos from './components/LikedVideos.vue';
const API_KEY = 'AIzaSyBpERjOxy3CUvcRHGyszuC3RQk_rSFUt-o';
export default {
  name: 'App',
  components: {
    BrowseVideos,
    LikedVideos
  },
  props:{
    likedVideosList: Array,
    searches: Object
  },
  data(){
    return{
      likedVideos : [],
      title: 'Browse Videos',
      searchedVideos: {}
    }
  },
  created(){
     this.getLikedVideos();
  },
  methods:{
    toggleComps(comp){
      const comp1 = document.querySelector('.comp1');
      const comp2 = document.querySelector('.comp2');
      if(comp === 'browse'){
        comp1.classList.remove('hidden');
        comp2.classList.add('hidden');
      }
      if(comp === 'likes'){
        comp2.classList.remove('hidden');
        comp1.classList.add('hidden');
      }
    },
     getLikedVideos: async function(){
      const response = await fetch('http://127.0.0.1:8000/api/likes');
      const data = await response.json();
      this.likedVideos = data;
    },
    async getVideosFromYoutube(query){
      const response = await fetch(`https://www.googleapis.com/youtube/v3/search?part=snippet&q=${query}&key=${API_KEY}`);
      const data = await response.json();
      this.searchedVideos = data;
      console.log(data);
    },
    async likeVideo(video){
      console.log(video);
      const data = {
        name: video.snippet.title,
        uploader: video.snippet.channelTitle,
        thumbnail: video.snippet.thumbnails.default.url
      };
       await fetch('http://127.0.0.1:8000/api/likes/',{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
       this.getLikedVideos();
    },
    async unlinkVideoFn(video){
      console.log(video);
      const data = {
        name: video.name,
        uploader: video.uploader,
        thumbnail: video.thumbnail
      };
      await fetch(`http://127.0.0.1:8000/api/likes/${video.id}`,{
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      this.getLikedVideos();
    }
  }
}
</script>
<style>
.hidden{
      display: none;
    }
</style>
<style scoped>
    *{
      font-family: 'Arial', sans-serif;
    }
    
    .container{
        width: 640px;
        margin: 100px auto;
        border: 1px solid #bbb;
        border-radius: 4px;        
    }
    .app_head{
        display: flex;
        width: calc(100% - 20px);
        justify-content: space-between;
        align-items: center;
        padding-left: 10px;
    }
    h1{
        font-size: 18pt;
        font-weight: lighter;
        display: inline-block;
    }
    .link_list{
        list-style:none;
        display: flex;     
    }
    li{
        padding: 5px 10px;
        border-bottom: 2px solid transparent;
    }
    li:hover{
      border-bottom: 2px solid rgb(8, 151, 8);
    }
    .link_li{
      border-bottom: 2px solid rgb(8, 151, 8);
    }
</style>
