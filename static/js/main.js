function like(id_song, id_user, el){
    $.ajax({
        url: "/song/like/",
        data: {
            'id_song':id_song,
            'id_user':id_user
        },

        dataType: 'json',
        success: function (data) {
            const song_likes = JSON.parse(data.song_likes);
            const all_users = JSON.parse(data.all_users);
            console.log(all_users);
            $('#song_' + id_song + ' > div > div:nth-child(4) > div > span > span').html(song_likes);
        }
    });
}

function showModal(el){
    const modal = el.firstElementChild;
    modal.style.cssText = "visibility:visible; opacity:1;";
}

function hideModal(el){
    const modal = el.firstElementChild;
    modal.style.cssText = "visibility: hidden; opacity:0;";
}