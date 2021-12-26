import axios from "axios"

const recommendations = {
    team: async (team) => {
        return await axios.get(`http://127.0.0.1:8080/recommend/${team}`)
    }
}

export default recommendations