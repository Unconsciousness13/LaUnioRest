const API_URL_GYMNASTS = "http://127.0.0.1:8000/api/gymnasts/";


export const gymnastsList = async () => {
    return await fetch(API_URL_GYMNASTS);
}