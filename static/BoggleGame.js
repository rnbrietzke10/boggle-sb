class BoggleGame {
  constructor() {
    this.duration = 60;
    this.playerData = {
      highScore: 0,
      timesPlayed: 0,
    };
    this.score = 0;
  }
  async sendGameData() {
    const response = await axios({
      method: "post",
      url: "http://127.0.0.1:5000/player-data",
      data: {
        gameData: this.gameData(this.score),
      },
    });
    return response.data;
  }

  timer() {
    const interval = setInterval(function () {
      timeRemaining -= 1;
      $("#seconds-remaining").text(timeRemaining);
    }, 1000);
    setTimeout(function () {
      clearInterval(interval);
      // await this.sendGameData();
      $submitBtn.attr("disabled", true);
    }, 60000);
  }

  async sendWord() {
    const response = await axios({
      method: "post",
      url: "http://127.0.0.1:5000/user-word",
      data: {
        word: $userWord.val(),
      },
    });
    return response.data;
  }

  gameData(score) {
    this.playerData["highScore"] =
      score > this.playerData["highScore"]
        ? score
        : this.playerData["highScore"];
    this.playerData["timesPlayed"] = this.playerData["timesPlayed"] + 1;
    return this.playerData;
  }
}
