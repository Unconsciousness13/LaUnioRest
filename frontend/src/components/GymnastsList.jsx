import React from "react";
import { useEffect, useState } from "react";
import * as GymnastList from "./GymnastsServer";

export default function GymnastsList() {
  const [gymnasts, setGymnasts] = useState([]);
  const gymnastsList = async () => {
    try {
      const res = await GymnastList.gymnastsList();
      const data = await res.json();
      setGymnasts(data);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    gymnastsList(gymnasts);
  }, []);
  return (
    <div>
      {gymnasts.map((gymnast) => (
        <div>
          <p>{gymnast.first_name}</p>
          <p>{gymnast.last_name}</p>
          <p>{gymnast.category}</p>
          <p>{gymnast.train}</p>
          <p>{gymnast.birthdate}</p>
          <p>{gymnast.description}</p>
          <img style={{width: '300px', height: '200px'}} src={"https://res.cloudinary.com/hifaleo6q/" + gymnast.photo} alt="gymnast" />
          
          <p>{gymnast.team}</p>
        </div>
      ))}
    </div>
  );
}
