import axios from "axios"
import { common } from "../config"

const endpoints = {
    edit: async (recommentation, data) => {
        return await axios.put(`${common.API.backend}/${recommentation}`, data)
    },
    delete: async (recommentation) => {
        return await axios.put(`${common.API.backend}/${recommentation}`)
    },
    recommendation: async (id) => {
        return await axios.get(`${common.API.backend}/recommend/${id}`)
    },
    team: async (team) => {
        return await axios.get(`${common.API.backend}/team/${team}/`)
    }
}

const dummies = {
    recommendation: () => ({
        data: {
            "id": 1,
            "recommendation": 10101,
            "team": 1,
            "created_at": "2021-12-27T03:32:19Z",
            "status": "current",
            "recommendation_headline": "Veniam quis nulla anim sunt nulla.",
            "team_name": "Team 1"
        }
    }),
    team: () => ({
        data: [
            {
                "id": 1,
                "recommendation": 10101,
                "team": 1,
                "created_at": "2021-12-27T03:32:19Z",
                "status": "current",
                "recommendation_headline": "Veniam quis nulla anim sunt nulla.",
                "team_name": "Team 1"
            },
            {
                "id": 2,
                "recommendation": 10101,
                "team": 1,
                "created_at": "2021-12-27T03:32:19Z",
                "status": "current",
                "recommendation_headline": "Ullamco pariatur enim consectetur tempor dolore do.",
                "team_name": "Team 1"
            },
            {
                "id": 3,
                "recommendation": 10101,
                "team": 1,
                "created_at": "2021-12-27T03:32:19Z",
                "status": "current",
                "recommendation_headline": "Eu anim fugiat et fugiat dolore fugiat quis commodo laboris.",
                "team_name": "Team 1"
            },
            {
                "id": 4,
                "recommendation": 10101,
                "team": 1,
                "created_at": "2021-12-27T03:32:19Z",
                "status": "implemented",
                "recommendation_headline": "Cillum incididunt elit deserunt ex commodo nostrud.",
                "team_name": "Team 1"
            },
            {
                "id": 5,
                "recommendation": 10101,
                "team": 1,
                "created_at": "2021-12-27T03:32:19Z",
                "status": "implemented",
                "recommendation_headline": "Quis incididunt eiusmod et tempor velit fugiat commodo consequat fugiat.",
                "team_name": "Team 1"
            },
            {
                "id": 6,
                "recommendation": 10101,
                "team": 1,
                "created_at": "2021-12-27T03:32:19Z",
                "status": "unapplicable",
                "recommendation_headline": "Quis incididunt eiusmod et tempor velit fugiat commodo consequat fugiat.",
                "team_name": "Team 1"
            },
        ]
    })
}

const recommendations = common.API.overrideDummies ? {...endpoints, ...dummies} : endpoints

export default recommendations