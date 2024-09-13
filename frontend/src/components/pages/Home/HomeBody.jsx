import {
  HomePage,
  HomePageContentBG,
  HomePageDescription,
  HomePageImage,
  HomePageIntroImage,
} from "../../../styles/components/HomeBody";
import { Title } from "../../../styles/components/Title";
import { Description } from "../../../styles/components/Description";
import InputFieldGetStarted from "../../common/InputFieldGetStarted";

function HomeBody() {
  return (
    <HomePage>
      <HomePageContentBG>
        <HomePageDescription>
          <Title fontSize={"40px"}>Build with</Title>
          <Title>AgentSmiths</Title>
          <Description>
            Hey there, welcome to AgentSmiths!
            <br />
            Creating your dream website is now a breeze with our friendly
            agents. No more headaches with complicated codes or dull designs.
            Let AgentSmiths craft a site for you that's not only responsive and
            high-performing but also tailored to your unique style and needs.
            Say goodbye to the hassle and hello to your amazing new website in
            just seconds!
            <br />
          </Description>
          <InputFieldGetStarted />
        </HomePageDescription>
        <HomePageIntroImage>
          <HomePageImage src="HomePage1.gif" alt="Description of the image" />
        </HomePageIntroImage>
      </HomePageContentBG>

      <HomePageContentBG>
        <HomePageIntroImage>
          <HomePageImage src="HomePage2.gif" alt="Description of the image" />
        </HomePageIntroImage>
        <HomePageDescription>
          <Title fontSize={"40px"}>What’s so</Title>
          <Title>Different?</Title>
          <Description>
            Ready to make your dream website a reality?
            <br />
            Simply chat with our friendly AgentSmiths agent to share your ideas.
            Forget the hassle of traditional website building. Within seconds,
            you'll have a unique site customized just for you. Enjoy the freedom
            to tweak its look and add new features whenever you please. And the
            best part? Making future changes is a breeze! Just log in to your
            user space and update your website with ease.
            <br />
          </Description>
          <InputFieldGetStarted />
        </HomePageDescription>
      </HomePageContentBG>

      <HomePageContentBG>
        <HomePageDescription>
          <Title fontSize={"40px"}>What we</Title>
          <Title>Facilitate</Title>
          <Description>
            "Step into the world of AgentSmiths and discover the magic of
            captivating UI designs for an amazing user experience. Our optimized
            coding ensures a smooth and efficient workflow for your website.
            With the AgentSmiths platform, you can keep an eye on user
            activities without any hassle. <br />
          </Description>
          <InputFieldGetStarted />
        </HomePageDescription>
        <HomePageIntroImage>
          <HomePageImage src="HomePage3.gif" alt="Description of the image" />
        </HomePageIntroImage>
      </HomePageContentBG>
    </HomePage>
  );
}

export default HomeBody;
