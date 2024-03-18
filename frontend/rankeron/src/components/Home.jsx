import React, { useEffect, useState } from "react";
import UserCard from "./UserCard";

function Home() {
  const [users, setUsers] = useState([]);

  const getUser = async () => {
    const response = await fetch("http://127.0.0.1:8000/rank/rankers/");
    const data = await response.json();
    setUsers(data.results);
    console.log(data.results);
  };

  useEffect(() => {
    getUser();
  }, []);

  const reloadData = () => {
    getUser(); 
  };

  return (
    <div className="flex flex-wrap">
      {users.map((curElem) => {
        return (
          <div key={curElem.user} className="w-full md:w-1/2 lg:w-1/4 p-2">
            <UserCard data={curElem} reloadData={reloadData}/>
          </div>
        );
      })}
    </div>
   
  );
}

export default Home;
