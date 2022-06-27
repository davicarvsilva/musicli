function like(id_song, id_user){
    $.ajax({
        url: "/song/like/",
        data: {
            'id_song':id_song,
            'id_user':id_user
        },

        dataType: 'json',
        success: function (data) {
            const song_likes = JSON.parse(data.song_likes);

            $('#song_' + id_song + ' div.song-post-body div:last span.song-likes').html(song_likes);
        }
    });
}