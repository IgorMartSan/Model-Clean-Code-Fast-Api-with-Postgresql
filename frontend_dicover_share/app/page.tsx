import Image from "next/image";

import Feed from "./components/Feed";

export default function Home() {
  return (
    <section className="w-full flex-center flex-col">
      <h1 className="head_text text-center text-4xl text-b font-extrabold">Dicover & Share
        <br className="max-2xl::hidden" />
        <span className="purple_orange_gradient"> AI-Powered Pronpts </span>

      </h1>
      <p className="text-center desc"> Lorem ipsum dolor sit, amet consectetur adipisicing elit. Beatae deserunt, voluptatem quisquam ad nemo nisi. Temporibus veritatis maiores a excepturi ipsa id odit deserunt. Obcaecati reprehenderit nam laudantium mollitia necessitatibus?</p>
      <Feed/>
    </section>
  );
}
