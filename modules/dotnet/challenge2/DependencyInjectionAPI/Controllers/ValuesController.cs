using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace DependencyInjectionAPI.Controllers
{
    [Route("api")]
    [ApiController]
    public class ValuesController : ControllerBase
    {
        
        [HttpGet]
        [Route("api/logger")]
        public ActionResult Logger()
        {
            // Demonstrate a Logger being used
            throw new NotImplementedException();
            return StatusCode(200);
        }

        [HttpGet]
        [Route("api/httpcontext")]
        public ActionResult HttpContext()
        {
            // Demonstrate a HttpContext being accessed in TestModel
            TestModel model = new TestModel();
            throw new NotImplementedException();
            return StatusCode(200);
        }

        [HttpGet]
        [Route("api/configuration")]
        public ActionResult Configuration()
        {
            // Demonstrate a Configuration values being used (must come from appsettings.ini)
            throw new NotImplementedException();
            return StatusCode(200);
        }

        [HttpGet]
        [Route("api/configuration")]
        public ActionResult CustomDependencyInjection()
        {
            // Have fun playing with Dependency Injection
            throw new NotImplementedException();
            return StatusCode(200);
        }
    }
}
