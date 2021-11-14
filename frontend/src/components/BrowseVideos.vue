<template>
    <div class="comp1">
        <input @input="getSearchResults"/>
       
        <ul>
            <li v-for="video in searches.items" :key="video.etag">
                <img :src="video.snippet.thumbnails.default.url">
                <div>
                    <h2>{{video.snippet.title}}</h2>
                    <p>{{video.snippet.channelTitle}}</p>
                    <button @click="transmitVideoData(video)">Like</button>
                </div>                
            </li>
        </ul>
    </div>    
</template>
<script>
    export default{
        name: 'BrowseVideos', 
        props: ['searches'],     
        methods:{
           getSearchResults(e){
                this.$emit('searchTerm',e.target.value);
            },
            transmitVideoData(video){
                this.$emit('videoLike',video);
            }
        }
    }
</script>
<style scoped>
*{
    margin-left: 10px;
}
input{
    width: calc(100% - 30px);
    height: 32px;
}
ul{
    list-style: none; 
    width: 100%;
    margin-left: -50px;   
    max-height: 40vh;
    overflow-x: hidden;
    overflow-y: auto;
}
li{
        display: flex;
        align-items: center;
    }
.thumb{
        width: 120px;
        height:80px;
        margin-right: 15px;
    }
</style>