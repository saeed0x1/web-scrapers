import cheerio from "cheerio";
import fetch from "node-fetch";

const scrapedDetails = async () => {
  try {
    const res = await fetch("https://mumbai.craigslist.org/search/sof");
    const data = await res.text();

    const $ = cheerio.load(data);

    const jobDetails = [];

    $(".result-info").each((i, e) => {
      const jobTitle = $(e).children(".result-heading").text().trim();
      const jobUrl = $(e)
        .children(".result-heading")
        .children("a")
        .attr("href");
      const date = $(e).children("time").attr("datetime");
      const jobNeighbour = $(e)
        .find(".result-meta")
        .children(".result-hood")
        .text()
        .trim();

      const scrapeRes = { jobTitle, jobUrl, jobNeighbour, date };
      jobDetails.push(scrapeRes);
    });
    return jobDetails;
  } catch (error) {
    console.error(error);
  }
};

const scrapeDescription = async (scrapedDetails) => {
  return await Promise.all(
    scrapedDetails.map(async (jobdes) => {
      try {
        const desPage = await fetch(jobdes.jobUrl);
        const data = await desPage.text();

        const $ = await cheerio.load(data);

        $(".print-information").remove();
        const comText = $(".attrgroup").children().first().text();
        jobdes.compensation = comText.replace("compensation: ", "");
        jobdes.description = $("#postingbody").text().trim();
        return jobdes;
      } catch (err) {
        console.error(err);
      }
    })
  );
};

const finalList = async () => {
  const job = await scrapedDetails();
  const final = await scrapeDescription(job);
  console.log(final);
};

finalList();
