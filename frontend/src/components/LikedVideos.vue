<template>
    <ul class="comp2 hidden">
        <li v-for="likedVideo in likedVideosList" :key="likedVideo.name">
            <img class="thumb" :src="likedVideo.thumbnail" />
            <div class="video-details">
                <h2>{{likedVideo.name}}</h2>
                <p>{{likedVideo.uploader}}</p>
                <button @click="transmitDelete(likedVideo)">Unlike</button>
            </div>
        </li>
    </ul>
</template>
<script>
    export default {
        name: 'LikedVideos',
        props: ['likedVideosList'],
        methods:{
            transmitDelete(video){
                this.$emit('unlikeVideo',video);
            },
        }
    }
</script>
<style scoped>
ul{
    display: block;
}
    li{
        display: flex;
        align-items: center;
    }
    .hidden{
      display: none;
    }
    .thumb{
        width: 120px;
        height:80px;
        margin-right: 15px;
    }
</style>