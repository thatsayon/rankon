import React from "react";
import { FaFacebook, FaArrowUp } from "react-icons/fa";

function UserCard({ data, reloadData }) {
    const handleUpvote = async (userId, reloadData) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/rank/vote/${userId}/`, {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({}),
            });
            if (!response.ok) {
              throw new Error("Failed to upvote");
            }
            reloadData();
          } catch (error) {
            console.error("Error upvoting:", error);
          }
    }
  return (
    <>
      <a
        href="#"
        className="flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700"
      >
        <img
          className="object-cover w-full rounded-t-lg h-96 md:h-auto md:w-48 md:rounded-none md:rounded-s-lg"
          src={"http://127.0.0.1:8000" + data.image}
          alt=""
        />
        <div className="flex flex-col justify-between p-4 leading-normal">
          <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
            {data.full_name}
          </h5>
          <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">
            <b>Total Vote: </b> {data.vote}
          </p>
          <div className="flex items-center justify-between">
            <a
              href={data.facebook}
              className="text-blue-500 hover:text-blue-700"
            >
              <FaFacebook className="w-6 h-6 mr-1" />
            </a>
            <button onClick={() => handleUpvote(data.user, reloadData)} className="text-gray-500 hover:text-gray-700">
              <FaArrowUp className="w-6 h-6" />
            </button>
          </div>
        </div>
      </a>
    </>
  );
}

export default UserCard;
