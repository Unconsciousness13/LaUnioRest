const API_URL_TRAINERS = "http://127.0.0.1:8000/api/trainers/";


export const trainersList = async () => {
    return await fetch(API_URL_TRAINERS);
}