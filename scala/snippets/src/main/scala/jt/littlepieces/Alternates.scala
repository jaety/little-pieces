package jt.littlepieces

object Alternates {
	def alternates(s: String): Seq[String] = s match {
	  case "a" => Seq("a","b","c")
      case "d" => Seq("d","e","f")
      case "g" => Seq("g","h","i")
    }

	def allLists(prefix: Seq[String], input: Seq[String]) : Seq[Seq[String]] = {
		input.headOption match {
			case None => Seq(prefix)
			case Some(w) => alternates(w).flatMap(alt => allLists(prefix :+ alt, input.tail))
        }
    }

	def main(args: Array[String]): Unit = {
		val input = Seq("a","d","g")
		println("input")
		println(input)
		println("outputs")
		allLists(Seq.empty, input).foreach(println)
	}
}
