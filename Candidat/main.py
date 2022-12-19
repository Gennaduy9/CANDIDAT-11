from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route("/")
def index():
    candidates = utils.get_candidates_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate_by_pk(pk)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidates_bu_name(candidate_name):
    candidates = utils.get_candidates_bu_name(candidate_name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill>")
def get_candidates_bu_skills(skill):
    candidates = utils.get_candidates_by_skill(skill.lower())
    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates))

if __name__ == '__main__':
    app.run(port=7000, debug=True)



