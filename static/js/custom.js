let dislike = $("#dislike")
let like = $("#like")

let dislikeUrl = dislike.attr("data-url")
let likeUrl = like.attr("data-url")



dislike.click(function(){


    $.ajax({
        url: dislikeUrl,
        type: "GET",
        dataType: "json",
        success: (data) => {
            if (data.success){
              $("#like-count").html(data.likes)
              $("#dislike-count").html(data.dislikes)
              $("#success").html(data.message)
            } else {
              $("#warning").html(data.message)
          }
        },
        error: (error) => {
          console.log(error);
        }
      });
})

like.click(function(){
    $.ajax({
        url: likeUrl,
        type: "GET",
        dataType: "json",
        success: (data) => {
          if (data.success){
            $("#like-count").html(data.likes)
            $("#dislike-count").html(data.dislikes)
            $("#success").html(data.message)
          } else {
            $("#warning").html(data.message)
          }
        },
        error: (error) => {
          console.log(error);
        }
      });
})