const $submitBtn = $('#submit-word-btn');
const $userWord = $('#user-word');
let correctAnswer = '';

const game = new BoggleGame();
let words_submitted = 0;
$('#seconds-remaining').text(game.duration);

timeRemaining = parseInt($('#seconds-remaining').text());

async function handleWordSubmit(evt) {
  evt.preventDefault();
  if (words_submitted === 0) {
    game.timer();
  }
  words_submitted += 1;
  correctAnswer = await game.sendWord();
  showAnswerMessage(correctAnswer);
  $userWord.val('');
}

$submitBtn.on('click', handleWordSubmit);

if (localStorage.getItem('score') === null) {
  game.score = 0;
  $('#score').text(game.score);
} else {
  game.score = parseInt(localStorage.getItem('score'));
  $('#score').text(game.score);
}

function showAnswerMessage(obj) {
  const { result } = obj;
  if (result === 'ok') {
    // Show Correct, you earned 1 point
    game.score += result.length;
    localStorage.setItem('score', game.score);
    $('#score').text(game.score);
    $('#content').append(
      `<h2 class ="show-result">Great Job! You earned ${result.length} points</h2>`
    );
  } else if (result === 'not-on-board') {
    // Show Word not on board
    $('#content').append(
      '<h2 class ="show-result">Sorry, that word is not on the board</h2>'
    );
  } else {
    // Show Sorry that's not a word
    $('#content').append(
      `<h2 class ="show-result">Sorry, that's not a word</h2>`
    );
  }
  setTimeout(function () {
    $('.show-result').remove();
  }, 5000);
}

// $('#new-game').on('click', function () {
//   console.log('Clicked');
//   words_submitted = 0;
//   game.sendGameData();
//   game.duration = 60;
//   game.score = 0;
//   $('#score').text(game.score);
//   localStorage.setItem('score', game.score);
// });
