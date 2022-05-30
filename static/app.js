const $submitBtn = $("#submit-word-btn");
const $userWord = $("#user-word");
let correctAnswer = "";
async function handleWordSubmit(evt) {
  evt.preventDefault();
  console.log($userWord.val());
  correctAnswer = await sendWord();
  showAnswerMessage(correctAnswer);
  $userWord.val("");
}

$submitBtn.on("click", handleWordSubmit);

async function sendWord() {
  const response = await axios({
    method: "post",
    url: "http://127.0.0.1:5000/user-word",
    data: {
      word: $userWord.val(),
    },
  });
  console.log(response.data);
  return response.data;
}

function showAnswerMessage(obj) {
  const { result } = obj;
  console.log("Result: " + result);
  if (result === "ok") {
    // Show Correct, you earned 1 point
    $("#content").append(
      '<h2 class ="show-result">Great Job! You earned 1 point</h2>'
    );
  } else if (result === "not-on-board") {
    // Show Word not on board
    $("#content").append(
      '<h2 class ="show-result">Sorry, that word is not on the board</h2>'
    );
  } else {
    // Show Sorry that's not a word
    $("#content").append(
      `<h2 class ="show-result">Sorry, that's not a word</h2>`
    );
  }
  setTimeout(function () {
    $(".show-result").remove();
  }, 5000);
}
