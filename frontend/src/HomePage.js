import { Button, Input, colors} from "@mui/material";
const HomePage = () => {
    return(
        <div className="HomePage" >

        <div className="HomePage-ContentBG">
            <div className="HomePage-Description">
                <span style={{fontSize: 60, lineHeight: 1.2}}>Build with<br/>AgentSmiths<br/></span>
                <div className="HomePage-Description-Paragraph">
                Hey there, welcome to AgentSmiths!<br/>
                Creating your dream website is now a breeze with our friendly agents. 
                No more headaches with complicated codes or dull designs. 
                Let AgentSmiths craft a site for you that's not only responsive and 
                high-performing but also tailored to your unique style and needs. 
                Say goodbye to the hassle and hello to your amazing new website in just seconds!<br/>
                </div>
                <div className="HomePage-Description-Input">
                    <Input type="text" className="Input-Field" placeholder="Type your website's domain..."/>
                    <Button className="GetStarted" type="submit">Get Started &lt; &gt;</Button>
                </div>
            </div>
            <div className="HomePage-IntroImage">
                <img src="HomePageIntro2.png" alt="Description of the image" class="HomePage-Image"/>
            </div>
        </div>

        <div className="HomePage-ContentBG">
            <div className="HomePage-IntroImage">
                <img src="HomePageIntro.png" alt="Description of the image" class="HomePage-Image"/>
            </div>
            <div className="HomePage-Description">
                <span style={{fontSize: 60, lineHeight: 1.2}}>What’s so<br/>Different?<br/></span>
                <div className="HomePage-Description-Paragraph">
                Ready to make your dream website a reality?<br/>
                Simply chat with our friendly AgentSmiths agent to share your ideas. 
                Forget the hassle of traditional website building. Within seconds, 
                you'll have a unique site customized just for you. 
                Enjoy the freedom to tweak its look and add new features whenever you please. 
                And the best part? Making future changes is a breeze! 
                Just log in to your user space and update your website with ease.<br/>
                </div>
                <div className="HomePage-Description-Input">
                    <Input type="text" className="Input-Field" placeholder="Type your website's domain..."/>
                    <Button className="GetStarted" type="submit">Get Started &lt; &gt;</Button>
                </div>
            </div>
        </div>

        <div className="HomePage-ContentBG">
            <div className="HomePage-Description">
                <span style={{fontSize: 60, lineHeight: 1.2}}>What we<br/>Facilitate<br/></span>
                <div className="HomePage-Description-Paragraph">
                "Step into the world of AgentSmiths and discover the magic of captivating UI designs 
                for an amazing user experience. 
                Our optimized coding ensures a smooth and efficient workflow for your website.  
                With the AgentSmiths platform, you can keep an eye on user activities without any hassle. <br/>
                </div>
                <div className="HomePage-Description-Input">
                    <Input type="text" className="Input-Field" placeholder="Type your website's domain..."/>
                    <Button className="GetStarted" type="submit">Get Started &lt; &gt;</Button>
                </div>
            </div>
            <div className="HomePage-IntroImage">
                <img src="HomePageFeatures.png" alt="Description of the image" class="HomePage-Image"/>
            </div>
        </div>

        </div>
    );
}

export default HomePage;